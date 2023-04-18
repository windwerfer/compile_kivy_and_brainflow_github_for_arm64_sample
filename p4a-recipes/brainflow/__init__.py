from pythonforandroid.recipe import PythonRecipe

class BrainflowRecipe(PythonRecipe):
    version = '9.9.9'
    url = 'https://github.com/windwerfer/compile_kivy_with_github_sample/raw/main/p4a-recipes/brainflow/brainflow-{version}.tar.gz'
    name = 'brainflow'
    depends = ['nptyping', 'numpy']
    md5sum = '53e1ca801ca5a8641a6cc21c7ca48e26'

recipe = BrainflowRecipe()
