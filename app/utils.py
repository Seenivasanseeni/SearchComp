from app.models import Organization

def searchMission(mission):
	result={"orgs":[],"len":0}
	for org in Organization.query.all():
		if org.mission==mission:
			result["orgs"].append(org)
			result["len"]+=1
	return result