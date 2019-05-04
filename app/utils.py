from app.models import Organization
from math import log2

def searchMission(mission):
	result={"orgs":[],"len":0}
	orgs = Organization.query.all()
	for org in orgs:
		org_mission = org.mission
		for word in org_mission.split(" "):
			if word in mission.split(" "):
				result["orgs"].append(org)
				result["len"]+=1
				break
	return result