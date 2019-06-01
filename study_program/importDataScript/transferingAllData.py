import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

exec(open(os.path.join(BASE_DIR, '/study_program/importDataScript/createAssessmentResult.py'),encoding="utf8").read())

exec(open(os.path.join(BASE_DIR, '/study_program/importDataScript/createStudyProgramScript.py'),encoding="utf8").read())
exec(open(os.path.join(BASE_DIR, '/study_program/importDataScript/createProfessorScript.py'),encoding="utf8").read())
exec(open(os.path.join(BASE_DIR, '/study_program/importDataScript/createResponsibleProfessor.py'),encoding="utf8").read())

exec(open(os.path.join(BASE_DIR, '/study_program/importDataScript/createAUNResult.py'),encoding="utf8").read())
exec(open(os.path.join(BASE_DIR, '/study_program/importDataScript/createCommittee.py'),encoding="utf8").read())
exec(open(os.path.join(BASE_DIR, '/study_program/importDataScript/createCommitteeAssessment.py'),encoding="utf8").read())
exec(open(os.path.join(BASE_DIR, '/study_program/importDataScript/createAssessmentCommittee.py'),encoding="utf8").read())
exec(open(os.path.join(BASE_DIR, '/study_program/importDataScript/createUser.py'),encoding="utf8").read())