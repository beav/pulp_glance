import os
# NEED TO VERIFY


cirros_img_path = os.path.join(os.path.dirname(__file__), '../../../data/cirros-0.3.2-x86_64-disk.img')

# these are in correct ancestry order
busybox_ids = (
    '769b9341d937a3dba9e460f664b4f183a6cecdd62b337220a28b3deb50ee0a02',
    '48e5f45168b97799ad0aafb7e2fef9fac57b5f16f6db7f67ba2000eb947637eb',
    'bf747efa0e2fa9f7c691588ce3938944c75607a7bb5e757f7369f86904d97c78',
    '511136ea3c5a64f264b78b5433614aec563103b4d4702f3ba7d4d2698e22c158',
)
