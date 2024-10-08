import json
import os
import types
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tke.v20180525 import tke_client, models
try:
    SecretId = os.getenv('SecretId')
    SecretKey = os.getenv('SecretKey')
    clusterId = os.getenv('ClusterId')
    cred = credential.Credential(SecretId, SecretKey)
    # 实例化一个http选项，可选的，没有特殊需求可以跳过
    httpProfile = HttpProfile()
    httpProfile.endpoint = "tke.tencentcloudapi.com"

    # 实例化一个client选项，可选的，没有特殊需求可以跳过
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    # 实例化要请求产品的client对象,clientProfile是可选的
    client = tke_client.TkeClient(cred, "ap-shanghai", clientProfile)

    # 实例化一个请求对象,每个接口都会对应一个request对象
    req = models.DescribeClusterSecurityRequest()
    params = {
        "ClusterId": clusterId
    }
    req.from_json_string(json.dumps(params))

    # 返回的resp是一个DescribeClusterSecurityResponse的实例，与请求对象对应
    resp = client.DescribeClusterSecurity(req)
    # 输出json格式的字符串回包
    res = json.loads(resp.to_json_string())
    token=res["Password"]
    cacert=res["CertificationAuthority"]
    with open("/root/ca.crt", 'w', encoding='utf-8') as file:
      file.write(cacert)
    with open("/root/token", 'w', encoding='utf-8') as file:
      file.write(token)
except TencentCloudSDKException as err:
    print(err)
