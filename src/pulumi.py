import pulumi_cloudinit as cloudinit

resource_config = cloudinit.Config("resource", base64_encode=False,
                                   gzip=False,
                                   parts=[cloudinit.GetConfigPartArgs(
                                       content="baz",
                                       content_type="text/x-shellscript",
                                       filename="foobar.sh",
                                   )])