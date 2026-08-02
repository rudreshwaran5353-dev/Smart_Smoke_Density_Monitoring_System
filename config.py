"""
Configuration module for Smart Smoke Density Monitoring System.

This module contains all application-wide configuration settings including
database paths, API configurations, sensor thresholds, alert settings,
and other system parameters.

Author: Industrial Automation Team
Version: 1.0.0
"""

import os
from datetime import timedelta


class Config:
    """Base configuration class with common settings."""

    # Application Settings
    APP_NAME = "Smart Smoke Density Monitoring System"
    APP_VERSION = "1.0.0"
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key-change-in-production")

    # Flask Configuration
    FLASK_ENV = os.environ.get("FLASK_ENV", "production")
    JSON_SORT_KEYS = False
    JSON_COMPACT = False

    # Database Configuration
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATABASE_PATH = os.path.join(BASE_DIR, "database", "smoke.db")
    DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Session Configuration
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"

    # Sensor Configuration
    SENSOR_READ_INTERVAL = 1  # Seconds
    SENSOR_AVERAGING_SAMPLES = 10
    MQ2_SENSOR_PIN = 34  # ESP32 GPIO pin for MQ2 sensor
    MQ2_ADC_MAX_VALUE = 4095
    MQ2_CALIBRATION_VALUE = 9.83

    # Smoke Density Thresholds (in ppm - parts per million)
    SMOKE_THRESHOLD_WARNING = 30  # Yellow LED
    SMOKE_THRESHOLD_CRITICAL = 60  # Red LED
    SMOKE_THRESHOLD_SEVERE = 100  # All alerts activated

    # Alert Configuration
    ALERT_CHECK_INTERVAL = 1  # Seconds
    ALERT_COOLDOWN_PERIOD = 30  # Seconds between repeated alerts
    ALERT_SMS_ENABLED = True
    ALERT_BUZZER_ENABLED = True
    ALERT_RELAY_ENABLED = True

    # Relay & Fan Configuration
    RELAY_PIN = 25  # ESP32 GPIO pin for relay
    FAN_ENABLE_THRESHOLD = 30  # ppm
    FAN_AUTO_SHUTOFF_TIMEOUT = 300  # Seconds
    FAN_RAMP_UP_TIME = 2  # Seconds

    # Buzzer Configuration
    BUZZER_PIN = 26  # ESP32 GPIO pin for buzzer
    BUZZER_FREQUENCY = 1000  # Hz
    BUZZER_DURATION = 500  # Milliseconds

    # LED Configuration
    LED_GREEN_PIN = 12
    LED_YELLOW_PIN = 13
    LED_RED_PIN = 14
    LED_POWER_PIN = 27
    LED_BLINK_FREQUENCY = 0.5  # Hz

    # GSM/SMS Configuration
    GSM_MODULE_PIN = 17  # RX pin
    GSM_MODULE_PIN_TX = 16  # TX pin
    GSM_BAUD_RATE = 9600
    GSM_ENABLED = True
    SMS_ALERT_RECIPIENTS = []  # Will be loaded from database
    SMS_API_TIMEOUT = 10  # Seconds

    # WiFi Configuration
    WIFI_SSID = os.environ.get("WIFI_SSID", "")
    WIFI_PASSWORD = os.environ.get("WIFI_PASSWORD", "")
    WIFI_RECONNECT_INTERVAL = 30  # Seconds
    WIFI_CONNECTION_TIMEOUT = 20  # Seconds

    # ESP32 API Configuration
    ESP32_API_TIMEOUT = 5  # Seconds
    ESP32_HEARTBEAT_INTERVAL = 10  # Seconds
    ESP32_HEARTBEAT_TIMEOUT = 30  # Seconds
    DATA_UPDATE_ENDPOINT = "/api/update"
    DATA_HISTORY_LIMIT = 10000  # Maximum records per query

    # Dashboard Configuration
    DASHBOARD_REFRESH_INTERVAL = 1000  # Milliseconds
    CHART_MAX_DATA_POINTS = 1440  # 24 hours at 1 minute intervals
    CHART_UPDATE_FREQUENCY = 60  # Seconds
    LIVE_UPDATE_ENABLED = True

    # Data Retention Policy
    DATA_RETENTION_DAYS = 90  # Keep data for 90 days
    DATA_ARCHIVE_ENABLED = True
    DATA_CLEANUP_SCHEDULE = "0 2 * * *"  # 2 AM every day

    # Machine Learning Configuration
    ML_ENABLED = True
    ML_MODEL_PATH = os.path.join(BASE_DIR, "ml", "health_model.pkl")
    ML_ANOMALY_MODEL_PATH = os.path.join(BASE_DIR, "ml", "anomaly_model.pkl")
    ML_SCALER_PATH = os.path.join(BASE_DIR, "ml", "scaler.pkl")
    ML_PREDICTION_CONFIDENCE_THRESHOLD = 0.7
    ML_ANOMALY_SENSITIVITY = 0.95  # Standard deviations

    # Export & Reports Configuration
    EXPORT_FORMATS = ["csv", "json", "excel"]
    REPORTS_DIR = os.path.join(BASE_DIR, "reports")
    EXPORTS_DIR = os.path.join(BASE_DIR, "exports")
    REPORT_GENERATION_ENABLED = True

    # Logging Configuration
    LOG_LEVEL = "INFO"
    LOG_DIR = os.path.join(BASE_DIR, "logs")
    LOG_FILE = os.path.join(LOG_DIR, "app.log")
    LOG_MAX_SIZE = 10485760  # 10 MB
    LOG_BACKUP_COUNT = 5
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # API Rate Limiting
    RATE_LIMIT_ENABLED = True
    RATE_LIMIT_REQUESTS = 1000  # Requests
    RATE_LIMIT_PERIOD = 3600  # Seconds (1 hour)
    API_KEY_REQUIRED = False

    # UI/UX Configuration
    THEME_COLOR = "#1a1a2e"  # Dark industrial theme
    ACCENT_COLOR = "#00d4ff"  # Cyan accent
    CHART_COLOR_PALETTE = [
        "#00d4ff",  # Cyan
        "#ff006e",  # Pink
        "#ffbe0b",  # Yellow
        "#8338ec",  # Purple
        "#3a86ff",  # Blue
    ]
    LANGUAGE = "en"

    # System Health Monitoring
    SYSTEM_HEALTH_CHECK_INTERVAL = 60  # Seconds
    MEMORY_WARNING_THRESHOLD = 80  # Percentage
    DISK_WARNING_THRESHOLD = 85  # Percentage
    CPU_WARNING_THRESHOLD = 90  # Percentage

    # Database Optimization
    DATABASE_CACHE_SIZE = 2000
    DATABASE_QUERY_TIMEOUT = 30  # Seconds
    DATABASE_POOL_SIZE = 10
    DATABASE_POOL_RECYCLE = 3600


class DevelopmentConfig(Config):
    """Development environment configuration."""

    DEBUG = True
    TESTING = False
    SESSION_COOKIE_SECURE = False
    LOG_LEVEL = "DEBUG"
    RATE_LIMIT_ENABLED = False


class TestingConfig(Config):
    """Testing environment configuration."""

    TESTING = True
    DEBUG = True
    DATABASE_PATH = os.path.join(Config.BASE_DIR, "database", "test_smoke.db")
    DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
    SESSION_COOKIE_SECURE = False
    ML_ENABLED = False
    GSM_ENABLED = False


class ProductionConfig(Config):
    """Production environment configuration."""

    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    LOG_LEVEL = "WARNING"
    RATE_LIMIT_ENABLED = True
    API_KEY_REQUIRED = True


# Configuration dictionary for easy access
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}


def get_config():
    """
    Get the appropriate configuration based on the environment.

    Returns:
        Config: The configuration class for the current environment.
    """
    env = os.environ.get("FLASK_ENV", "development")
    return config.get(env, config["default"])
