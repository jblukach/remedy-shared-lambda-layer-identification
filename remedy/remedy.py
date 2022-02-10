import boto3
import json
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    
    client = boto3.client('ec2')
    regions = client.describe_regions()
    
    for region in regions['Regions']:
        
        lambda_client = boto3.client('lambda', region_name = region['RegionName'])
        
        paginator = lambda_client.get_paginator('list_layers')
        response_iterator = paginator.paginate()
        
        for page in response_iterator:
            for item in page['Layers']:
                    
                    paginator2 = lambda_client.get_paginator('list_layer_versions')
                    response_iterator2 = paginator2.paginate(LayerName = item['LayerName'])
                    
                    for page2 in response_iterator2:
                        for item2 in page2['LayerVersions']:
                            
                            print('Name: '+item['LayerName']+' Version: '+str(item2['Version']))
                            
                            try:
                                iam_policy = lambda_client.get_layer_version_policy(
                                    LayerName = item['LayerName'],
                                    VersionNumber = item2['Version']
                                )
                                print(iam_policy['Policy'])
                            except:
                                print('No Policy!')
                                pass

    return {
        'statusCode': 200,
        'body': json.dumps('Identify Shared Lambda Layers')
    }
