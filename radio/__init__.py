"""Micropython stubs for the microbit radio module"""

def on():
  """Turns the radio on. This needs to be explicitly called since the radio draws power and takes up memory that you may otherwise need."""
  return

def off():
  """Turns off the radio, thus saving power and memory."""
  return

def config(**kwargs):
  """Configures various keyword based settings relating to the radio.
  length=32, queue=3, channel=3, power=6, address=0x75626974, group=0
  """
  return

def reset():
  """Reset the settings to their default values"""
  return

def send_bytes(message):
  """Sends a message containing bytes."""
  return

def receive_bytes():
  """Receive the next incoming message on the message queue. Returns None if there are no pending messages. Messages are returned as bytes."""
  return

def receive_bytes(buffer):
  """Receive the next incoming message on the message queue. Copies the message into buffer, trimming the end of the message if necessary. Returns None if there are no pending messages, otherwise it returns the length of the message (which might be more than the length of the buffer)."""
  return

def send(message):
  """Sends a message string. This is the equivalent of send_bytes(bytes(message, 'utf8')) but with b'\x01\x00\x01' prepended to the front (to make it compatible with other platforms that target the micro:bit)."""

def receive():
  """Works in exactly the same way as receive_bytes but returns whatever was sent.
  Currently, it’s equivalent to str(receive_bytes(), 'utf8') but with a check that the the first three bytes are b'\x01\x00\x01' (to make it compatible with other platforms that may target the micro:bit). It strips the prepended bytes before converting to a string.
  A ValueError exception is raised if conversion to string fails."""
  return

def receive_full():
  """Returns a tuple containing three values representing the next incoming message on the message queue. If there are no pending messages then None is returned.
  (message, signal strength, microsecond timestamp from time.ticks_us)"""

RATE_250KBIT = 0
RATE_1MBIT = 1
RATE_2MBIT = 2