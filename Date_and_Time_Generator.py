# Print the following script:
# Today is "monday-sunday", "month date", "year"
from datetime import datetime

print(datetime.now().strftime("Today is %A, %B %d, %Y"))