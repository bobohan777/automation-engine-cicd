"""
Unit tests for utility functions
"""

from datetime import datetime, timedelta


from app.utils import calculate_uptime, format_response, sanitize_string, validate_input


class TestValidateInput:
    """Test validate_input function"""

    def test_valid_dict(self):
        """Test with valid dictionary"""
        data = {"key": "value"}
        assert validate_input(data) is True

    def test_valid_string(self):
        """Test with valid string"""
        data = "test string"
        assert validate_input(data) is True

    def test_valid_list(self):
        """Test with valid list"""
        data = [1, 2, 3]
        assert validate_input(data) is True

    def test_none_input(self):
        """Test with None input"""
        assert validate_input(None) is False

    def test_empty_dict(self):
        """Test with empty dictionary"""
        assert validate_input({}) is False


class TestFormatResponse:
    """Test format_response function"""

    def test_success_response(self):
        """Test successful response formatting"""
        data = {"message": "success"}
        result = format_response(data)

        assert result["success"] is True
        assert result["data"] == data
        assert "timestamp" in result

    def test_error_response(self):
        """Test error response formatting"""
        data = {"error": "something went wrong"}
        result = format_response(data)

        assert result["success"] is False
        assert result["data"] == data
        assert "timestamp" in result

    def test_timestamp_format(self):
        """Test timestamp is in ISO format"""
        data = {"test": "data"}
        result = format_response(data)

        # Should be able to parse the timestamp
        datetime.fromisoformat(result["timestamp"].replace("Z", "+00:00"))


class TestSanitizeString:
    """Test sanitize_string function"""

    def test_clean_string(self):
        """Test with clean string"""
        input_str = "clean string"
        result = sanitize_string(input_str)
        assert result == "clean string"

    def test_dangerous_characters(self):
        """Test removal of dangerous characters"""
        input_str = '<script>alert("xss")</script>'
        result = sanitize_string(input_str)
        assert "<" not in result
        assert ">" not in result
        assert "scriptalert(xss)/script" == result

    def test_non_string_input(self):
        """Test with non-string input"""
        result = sanitize_string(123)
        assert result == ""

    def test_whitespace_trimming(self):
        """Test whitespace trimming"""
        input_str = "  test string  "
        result = sanitize_string(input_str)
        assert result == "test string"


class TestCalculateUptime:
    """Test calculate_uptime function"""

    def test_recent_start_time(self):
        """Test with recent start time"""
        start_time = datetime.utcnow() - timedelta(seconds=30)
        result = calculate_uptime(start_time)

        assert "0d" in result
        assert "s" in result  # Should show seconds

    def test_hours_uptime(self):
        """Test with hours of uptime"""
        start_time = datetime.utcnow() - timedelta(hours=2, minutes=30)
        result = calculate_uptime(start_time)

        assert "0d" in result
        assert "2h" in result
        assert "30m" in result

    def test_days_uptime(self):
        """Test with days of uptime"""
        start_time = datetime.utcnow() - timedelta(days=1, hours=5)
        result = calculate_uptime(start_time)

        assert "1d" in result
        assert "5h" in result
