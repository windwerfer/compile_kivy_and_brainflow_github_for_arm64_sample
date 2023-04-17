
def get_recipe():
    return {
        'name': 'brainflow_arm64',
        'version': '5.7.1',  # specify the correct version number
        'source': {
            'type': 'file',
            'url': './brainflow_arm64_5.7.1.tar.gz',
            'md5sum': '804ef2e67bb920c0130bbff8de222351',
        },
        # ... other recipe details ...
    }
