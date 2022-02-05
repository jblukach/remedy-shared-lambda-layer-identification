#!/usr/bin/env python3
import os

import aws_cdk as cdk

from remedy_shared_lambda_layer_identification.remedy_shared_lambda_layer_identification_stack import RemedySharedLambdaLayerIdentificationStack

app = cdk.App()

RemedySharedLambdaLayerIdentificationStack(
    app, 'RemedySharedLambdaLayerIdentificationStack',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = os.getenv('CDK_DEFAULT_REGION')
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = '4n6ir'
    )
)

cdk.Tags.of(app).add('remedy-shared-lambda-layer-identification','remedy-shared-lambda-layer-identification')

app.synth()
