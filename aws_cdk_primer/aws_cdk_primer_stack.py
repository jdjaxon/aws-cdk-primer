"""Module for AWS CDK experimentation."""

import aws_cdk as cdk
import aws_cdk.aws_s3 as s3
from constructs import Construct

#pylint: disable=too-few-public-methods
class AwsCdkPrimerStack(cdk.Stack):
    """Class for defining AWS infrastructure."""

    #pylint: disable=useless-super-delegation
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "MyFirstBucket", versioned=True)
