from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.http import require_GET


@require_GET
def security_txt(request):
    lines = [{
  "relation": ["delegate_permission/common.handle_all_urls"],
  "target": {
    "namespace": "android_app",
    "package_name": "com.example.super_admin",
    "sha256_cert_fingerprints":
    ["F0:A2:7A:AD:50:17:6B:D3:7D:CF:9A:BE:33:B5:30:ED:74:09:FE:A1:12:5F:A1:66:AA:B7:DC:A6:58:20:D0:ED"]
  }
}]
    
    return HttpResponse((lines), content_type="json")