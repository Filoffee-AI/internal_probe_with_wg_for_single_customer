import meraki

# Your API key (ensure it's correctly secured and not hardcoded in production)
API_KEY = 'e7c8566fd6cc62171f2a36c5cd7dace6d091e4be'

dashboard = meraki.DashboardAPI(API_KEY)

serial = 'Q2FY-EZ6L-66NY'
target = '8.8.8.8'

# Adjusting the callback structure
response = dashboard.devices.createDeviceLiveToolsPing(
    serial, target,
    count=2,
    callback={
        'url': 'https://webhook.site/28efa24e-f830-4d9f-a12b-fbb9e5035031',
        'sharedSecret': 'secret',
        # Removed the 'httpServer' part
        'payloadTemplate': {'id': 'wpt_2100'}
    }
)

print(response)
