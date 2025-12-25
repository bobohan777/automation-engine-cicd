"""
Automation Engine - Flask Application
A simple web service demonstrating CI/CD pipeline integration
"""

from flask import Flask, jsonify, request
from datetime import datetime
import os
import logging
from .config import Config
from .utils import validate_input, format_response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def home():
    """Home endpoint returning service information"""
    return jsonify(format_response({
        'service': 'Automation Engine',
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'message': 'CI/CD Pipeline Demo - DevOps Engineering Excellence'
    }))


@app.route('/health')
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify(format_response({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'uptime': 'running'
    })), 200


@app.route('/api/echo', methods=['POST'])
def echo():
    """Echo endpoint for testing POST requests"""
    try:
        data = request.get_json()
        
        if not validate_input(data):
            return jsonify(format_response({
                'error': 'Invalid input data'
            })), 400
            
        return jsonify(format_response({
            'echo': data,
            'timestamp': datetime.utcnow().isoformat(),
            'processed': True
        }))
        
    except Exception as e:
        logger.error(f"Error in echo endpoint: {str(e)}")
        return jsonify(format_response({
            'error': 'Internal server error'
        })), 500


@app.route('/api/pipeline-info')
def pipeline_info():
    """Returns information about the CI/CD pipeline"""
    return jsonify(format_response({
        'pipeline': {
            'ci_stages': [
                'Code Checkout',
                'Python Linting (pylint, black, isort)',
                'Unit Tests (pytest)',
                'Docker Build',
                'Security Scan (Trivy)'
            ],
            'cd_stages': [
                'Docker Push to Hub',
                'Update K8s Manifests',
                'GitOps Deployment'
            ],
            'quality_gates': {
                'pylint_score': '≥ 8.0/10',
                'test_coverage': '≥ 80%',
                'security_scan': 'No HIGH/CRITICAL CVEs'
            },
            'technologies': [
                'GitHub Actions',
                'Docker',
                'Kubernetes',
                'Trivy Security Scanner',
                'Python Flask'
            ]
        },
        'build_info': {
            'commit_sha': os.getenv('GITHUB_SHA', 'local-dev'),
            'build_number': os.getenv('GITHUB_RUN_NUMBER', '0'),
            'branch': os.getenv('GITHUB_REF_NAME', 'main')
        }
    }))


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify(format_response({
        'error': 'Endpoint not found',
        'available_endpoints': [
            '/',
            '/health',
            '/api/echo',
            '/api/pipeline-info'
        ]
    })), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify(format_response({
        'error': 'Internal server error'
    })), 500


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    
    logger.info(f"Starting Automation Engine on port {port}")
    app.run(host='0.0.0.0', port=port, debug=debug)