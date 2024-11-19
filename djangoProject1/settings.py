"""
Configurações do Django para o projeto djangoProject1.

Gerado com 'django-admin startproject' usando Django 5.1.1.

Para mais informações, consulte
https://docs.djangoproject.com/en/5.1/topics/settings/

Para a lista completa de configurações e seus valores, consulte
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Definindo o diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configurações de desenvolvimento rápido - inadequado para produção
# Aviso: Mantenha a chave secreta protegida em produção!
SECRET_KEY = 'django-insecure-389nr@_d$ts6#j@n%@zs3$=src(y$#lnna4l94p=5rbwzxgu*0'

# Aviso: Não use o modo DEBUG ativado em produção!
DEBUG = True

# Hosts permitidos para o aplicativo. Em produção, adicione domínios ou IPs específicos
ALLOWED_HOSTS = []

# Definição de aplicativos instalados no projeto
INSTALLED_APPS = [
    'django.contrib.admin',            # App de administração do Django
    'django.contrib.auth',             # App de autenticação
    'django.contrib.contenttypes',     # Tipos de conteúdo do Django
    'django.contrib.sessions',         # Gerenciamento de sessões
    'django.contrib.messages',         # Mensagens do Django
    'django.contrib.staticfiles',      # Arquivos estáticos (CSS, JavaScript, imagens)
    "totem.apps.TotemConfig",          # Aplicativo customizado "totem"
]

# Configuração de middleware que lida com solicitações e respostas HTTP
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',               # Segurança em HTTPS e outras
    'django.contrib.sessions.middleware.SessionMiddleware',        # Middleware de sessão
    'django.middleware.common.CommonMiddleware',                   # Middleware de configuração comum
    'django.middleware.csrf.CsrfViewMiddleware',                   # Proteção CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',     # Middleware de autenticação
    'django.contrib.messages.middleware.MessageMiddleware',        # Middleware de mensagens
    'django.middleware.clickjacking.XFrameOptionsMiddleware',      # Proteção contra clickjacking
]

# URL raiz para mapeamento de URLs
ROOT_URLCONF = 'djangoProject1.urls'

# Configurações para renderização de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Motor de templates Django
        'DIRS': [],                                                    # Diretórios adicionais para templates
        'APP_DIRS': True,                                              # Carrega templates a partir dos apps
        'OPTIONS': {
            'context_processors': [                                    # Processadores de contexto
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuração para interface de servidor WSGI
WSGI_APPLICATION = 'djangoProject1.wsgi.application'

# Configuração de banco de dados MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # Backend do MySQL
        'NAME': 'totem',                        # Nome do banco de dados
        'USER': 'root',                         # Nome de usuário do banco
        'PASSWORD': 'Admin@801',                # Senha do banco
        'HOST': 'localhost',                    # Host do banco
        'PORT': '3306',                         # Porta do banco
    }
}

# Configuração para o uso de mídia (arquivos carregados pelo usuário)
MEDIA_URL = '/media/'                           # URL de acesso aos arquivos de mídia
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')    # Diretório de armazenamento dos arquivos

# Validações de senha para aumentar a segurança
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configurações de internacionalização
LANGUAGE_CODE = 'en-us'    # Código de idioma do projeto
TIME_ZONE = 'UTC'          # Fuso horário
USE_I18N = True            # Ativa internacionalização
USE_TZ = True              # Ativa uso de fuso horário

# Configurações para arquivos estáticos (CSS, JavaScript, etc.)
STATIC_URL = '/static/'    # URL de acesso aos arquivos estáticos
STATICFILES_DIRS = [       # Diretórios de arquivos estáticos adicionais
    BASE_DIR / "static",
]

# Configuração padrão para chave primária automática
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
