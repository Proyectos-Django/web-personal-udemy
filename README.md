=============================================================================
conda update -n base -c defaults conda

conda create -n py37 python=3.7.4

conda activate py37
conda deactivate

=============================================================================
conda create -n django3 python=3.7.4
conda activate django3
conda deactivate
pip install django==2.2.6

pip install django
pip list
django-admin startproject webpersonal

=============================================================================

python -m django --version => verfica la actual version de django
conda install pylint => comprobador de sintaxis

=============================================================================
python manage.py startapp core