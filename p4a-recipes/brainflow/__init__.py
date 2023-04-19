from pythonforandroid.recipe import PythonRecipe

class BrainflowRecipe(PythonRecipe):
    version = '9.9.9'
    url = 'https://raw.githubusercontent.com/windwerfer/compile_kivy_and_brainflow_github_for_arm64_sample/main/p4a-recipes/brainflow/brainflow-{version}-py3-none-any.whl'
    name = 'brainflow'
    depends = ['nptyping', 'numpy']
    md5sum = '53e1ca801ca5a8641a6cc21c7ca48e26'

recipe = BrainflowRecipe()

# test
# wget https://raw.githubusercontent.com/windwerfer/compile_kivy_and_brainflow_github_for_arm64_sample/main/p4a-recipes/brainflow/brainflow-9.9.9.tar.gz
