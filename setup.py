import setuptools

setuptools.setup(
    name="geochemsim-django-app",
    version="0.0.1",
    description="... description ...",
    packages=setuptools.find_packages(),
    install_requires=[
        'django>=2.2'
    ],
    entry_points="""
[airavata.djangoapp]
geochemsim_app = geochemsim_app.apps:GeochemsimAppConfig
""",
)
