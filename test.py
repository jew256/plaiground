import blpapi
import matplotlib.pyplot as plt
import numpy as np

# Create a session
session = blpapi.Session()

# Start a session
if not session.start():
    print("Failed to start session.")

# Open service to get historical data from
if not session.openService("//blp/refdata"):
    print("Failed to open //blp/refdata")

# Obtain previously opened service
refDataService = session.getService("//blp/refdata")

# Create and fill the request for the historical data
request = refDataService.createRequest("HistoricalDataRequest")

# Set the ticker
request.getElement("securities").appendValue("BZGD Index")

# Set the fields to get
request.getElement("fields").appendValue("PX_LAST")

# Set the start date and end date
request.set("startDate", "20000101")
request.set("endDate", "20100101")

# Set the periodicity
request.set("periodicitySelection", "MONTHLY")

# Send the request
session.sendRequest(request)

# Process received events
while(True):
    # We provide timeout to give the chance to Ctrl+C handling:
    ev = session.nextEvent(500)
    for msg in ev:
        print(msg)
        if msg.hasElement("securityData"):
            securityData = msg.getElement("securityData")
            fieldData = securityData.getElement("fieldData")
            for i in range(fieldData.numValues()):
                date = fieldData.getValue(i).getElementAsDatetime("date")
                gdp = fieldData.getValue(i).getElementAsFloat("PX_LAST")
                print(date, gdp)

# Plot the gdp
plt.plot(date, gdp)
plt.show()
