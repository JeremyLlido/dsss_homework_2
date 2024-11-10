from setuptools import setup, find_packages

setup(
    name="math_quiz",  # The name of your package
    version="0.1",     # Version of your package
    packages=find_packages(),  # Automatically find all packages in the current directory
    install_requires=[  # List any dependencies here (if any)
        # Example: 'numpy', 'requests', etc.
    ],
    entry_points={  # Makes it executable from the command line
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz',  # Point to the main function in your math_quiz.py
        ],
    },
    long_description=open('README.md').read(),  # Include your README file as the long description
    long_description_content_type='text/markdown',  # Use markdown format for the README
    author="Jeremy Llido",  # Replace with your name
    author_email="jeremy.llido@gmail.com",  # Replace with your email
    description="A simple math quiz game to practise mental arithmetic",  # Brief description of the project
    license="Apache",  # Choose an appropriate license
    url="https://github.com/JeremyLlido/dsss_homework_2.git",  # Link to your repository
)
