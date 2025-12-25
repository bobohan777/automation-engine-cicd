"""
Configuration module for Automation Engine
"""

import os


class Config:
    """Base configuration class"""
    
    # Flask settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    # Application settings
    APP_NAME = 'Automation Engine'
    APP_VERSION = os.getenv('APP_VERSION', '1.0.0')
    
    # API settings
    JSON_SORT_KEYS = False
    JSONIFY_PRETTYPRINT_REGULAR = True
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    # Security headers
    SECURITY_HEADERS = {
        'X-Content-Type-Options': 'nosniff',
        'X-Frame-Options': 'DENY',
        'X-XSS-Protection': '1; mode=block'
    }


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    LOG_LEVEL = 'DEBUG'


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    # For demo purposes, use a default secret key if not provided
    SECRET_KEY = os.getenv('SECRET_KEY', 'demo-secret-key-change-in-production')


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    SECRET_KEY = 'test-secret-key'


# Configuration mapping
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}