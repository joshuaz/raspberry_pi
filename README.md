THis raspberry pi project is for maintaining an appropriate humidity for my gourmet mushrooms.

Every 12 hours (set by cron job), the rasppi runs a script to check the humidity (using a DHT11 sensor).

If the humidity falls below 70%, it activates a humidifier (via a 3.3V relay).
