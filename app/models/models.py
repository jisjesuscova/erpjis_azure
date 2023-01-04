from flask_login import UserMixin
from app import db
from werkzeug.security import check_password_hash

class HrSingleTaxModel(db.Model):
    __tablename__ = 'hr_single_taxes'

    id = db.Column(db.Integer, primary_key=True)
    period = db.Column(db.String(20))
    since = db.Column(db.Float)
    until = db.Column(db.Float)
    factor = db.Column(db.Float)
    amount = db.Column(db.Float)
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class SettlementDatumModel(db.Model):
    __tablename__ = 'settlement_data'

    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer)
    visual_rut = db.Column(db.String(20))
    period = db.Column(db.String(20))
    support = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class TerminalModel(db.Model):
    __tablename__ = 'terminals'

    id = db.Column(db.Integer, primary_key=True)
    branch_office_id = db.Column(db.Integer)
    serial_number = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class EmployeeTypeModel(db.Model):
    __tablename__ = 'employee_types'

    id = db.Column(db.Integer, primary_key=True)
    employee_type = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())


class AttendancesModel(db.Model):
    __tablename__ = 'attendances'

    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer)
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class TurnModel(db.Model):
    __tablename__ = 'turns'

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer)
    group_day_id = db.Column(db.Integer)
    free_day_group_id = db.Column(db.Integer)
    employee_type_id = db.Column(db.Integer)
    turn = db.Column(db.String(255))
    working = db.Column(db.String(255))
    breaking = db.Column(db.String(255))
    start = db.Column(db.String(255))
    end = db.Column(db.String(255))
    break_in = db.Column(db.String(255))
    break_out = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class PreEmployeeTurnModel(db.Model):
    __tablename__ = 'pre_employees_turns'

    id = db.Column(db.Integer, primary_key=True)
    turn_id = db.Column(db.Integer)
    rut = db.Column(db.Integer)
    start_date = db.Column(db.Date())
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())


class HrUnemploymentInsuranceModel(db.Model):
    __tablename__ = 'hr_unemployment_insurances'

    id = db.Column(db.Integer, primary_key=True)
    employee_value = db.Column(db.Float)
    company_value = db.Column(db.Float)
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class HrHealthModel(db.Model):
    __tablename__ = 'hr_healths'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class EmployeeModel(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer)
    visual_rut = db.Column(db.String(20))
    names = db.Column(db.String(255))
    father_lastname = db.Column(db.String(255))
    mother_lastname = db.Column(db.String(255))
    nickname = db.Column(db.String(255))
    gender_id = db.Column(db.Integer)
    nationality_id = db.Column(db.Integer)
    cellphone = db.Column(db.String(100))
    born_date = db.Column(db.Date())
    picture = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class HrPentionModel(db.Model):
    __tablename__ = 'hr_pentions'

    id = db.Column(db.Integer, primary_key=True)
    pention_id = db.Column(db.Integer)
    period = db.Column(db.String(20))
    afp_value = db.Column(db.Float(150))
    sis_value = db.Column(db.Float(150))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class VacationModel(db.Model):
    __tablename__ = 'vacations'

    id = db.Column(db.Integer, primary_key=True)
    document_employee_id = db.Column(db.Integer)
    rut = db.Column(db.Integer)
    since = db.Column(db.Date())
    until = db.Column(db.Date())
    days = db.Column(db.Integer)
    no_valid_days = db.Column(db.Integer)
    support = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class RolModel(db.Model):
    __tablename__ = 'rols'

    id = db.Column(db.Integer, primary_key=True)
    rol = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class AuditModel(db.Model):
    __tablename__ = 'audits'

    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(255))
    model = db.Column(db.String(255))
    affected_rut = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())

class HrEmployeeDayModel(db.Model):
    __tablename__ = 'hr_employee_days'

    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer)
    period = db.Column(db.String(255))
    current_days = db.Column(db.Integer)
    entrance_days = db.Column(db.Integer)
    license_days = db.Column(db.Integer)
    exit_days = db.Column(db.Integer)
    absence_days = db.Column(db.Integer)
    adjustment_days = db.Column(db.Integer)
    days = db.Column(db.Integer)
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class EmployeeLaborDatumModel(db.Model):
    __tablename__ = 'employee_labor_data'

    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer)
    visual_rut = db.Column(db.String(20))
    contract_type_id = db.Column(db.Integer)
    branch_office_id = db.Column(db.Integer)
    region_id = db.Column(db.Integer)
    commune_id = db.Column(db.Integer)
    civil_state_id = db.Column(db.Integer)
    health_id = db.Column(db.Integer)
    pention_id = db.Column(db.Integer)
    job_position_id = db.Column(db.Integer)
    extreme_zone_id = db.Column(db.Integer)
    employee_type_id = db.Column(db.Integer)
    address = db.Column(db.String(255))
    entrance_company  = db.Column(db.Date())
    exit_company  = db.Column(db.Date())
    salary = db.Column(db.Integer)
    collation = db.Column(db.Integer)
    locomotion = db.Column(db.Integer)
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())


class HrFinalDayMonthModel(db.Model):
    __tablename__ = 'hr_final_day_months'

    id = db.Column(db.Integer, primary_key=True)
    end_day = db.Column(db.Integer)
    adjustment_day = db.Column(db.Integer)

class HrEmployeeInputModel(db.Model):
    __tablename__ = 'hr_employee_inputs'

    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.Integer)
    period = db.Column(db.String(20))
    branch_office_id = db.Column(db.Integer)
    hr_input_description_id = db.Column(db.Integer)
    value = db.Column(db.Integer)
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class HrInputDescriptionModel(db.Model):
    __tablename__ = 'hr_input_descriptions'

    id = db.Column(db.Integer, primary_key=True)
    hr_input_description = db.Column(db.String(255))
    settlement_name = db.Column(db.String(255))
    hr_input_type_id = db.Column(db.Integer)
    group_id = db.Column(db.Integer)
    header_position = db.Column(db.Integer)
    positive_position = db.Column(db.Integer)
    negative_position = db.Column(db.Integer)
    total_status = db.Column(db.Integer)
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class HrEmployeeLaborFieldModel(db.Model):
    __tablename__ = 'hr_employee_labor_fields'

    id = db.Column(db.Integer, primary_key=True)
    field = db.Column(db.String(255))
    hr_input_description_id = db.Column(db.Integer)
    hr_input_description_group_id = db.Column(db.Integer)
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class HrInputTypeModel(db.Model):
    __tablename__ = 'hr_input_types'

    id = db.Column(db.Integer, primary_key=True)
    hr_input_type = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class JobPositionModel(db.Model):
    __tablename__ = 'job_positions'

    id = db.Column(db.Integer, primary_key=True)
    job_position = db.Column(db.String(255))
    functions = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class CivilStateModel(db.Model):
    __tablename__ = 'civil_states'

    id = db.Column(db.Integer, primary_key=True)
    civil_state = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class GenderModel(db.Model):
    __tablename__ = 'genders'

    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())


class NationalityModel(db.Model):
    __tablename__ = 'nationalities'

    id = db.Column(db.Integer, primary_key=True)
    nationality = db.Column(db.String(255))
    previred_code = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class RegionModel(db.Model):
    __tablename__ = 'regions'

    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(255))    
    region_remuneration_code = db.Column(db.Integer) 
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class CommunesModel(db.Model):
    __tablename__ = 'communes'

    commune_id = db.Column(db.Integer, primary_key=True)
    region_id = db.Column(db.Integer)
    commune = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class StatusesModel(db.Model):
    __tablename__ = 'statuses'

    statuses_id = db.Column(db.Integer, primary_key=True)
    statuses_group_id = db.Column(db.Integer)
    statuses = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())


class DocumentTypeModel(db.Model):
    __tablename__ = 'document_types'

    id = db.Column(db.Integer, primary_key=True)
    document_type = db.Column(db.String(255))
    document_group_id = db.Column(db.Integer) 
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class DocumentGroupModel(db.Model):
    __tablename__ = 'document_groups'

    id = db.Column(db.Integer, primary_key=True)
    document_group = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class DocumentEmployeeModel(db.Model):
    __tablename__ = 'documents_employees'

    id = db.Column(db.Integer, primary_key=True)
    status_id = db.Column(db.Integer)
    document_type_id = db.Column(db.Integer)
    rut = db.Column(db.String(20))
    support = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())


class ContractTypeModel(db.Model):
    __tablename__ = 'contract_type'

    id = db.Column(db.Integer, primary_key=True)
    contract_type = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())


class HealthModel(db.Model):
    __tablename__ = 'healths'

    id = db.Column(db.Integer, primary_key=True)
    health_remuneration_code = db.Column(db.Integer)
    health = db.Column(db.String(255))
    rut = db.Column(db.String(20))
    previred_code = db.Column(db.Integer)
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())


class PentionModel(db.Model):
    __tablename__ = 'pentions'

    id = db.Column(db.Integer, primary_key=True)
    pention = db.Column(db.String(255))
    pention_remuneration_code = db.Column(db.Integer)
    rut = db.Column(db.String(20))
    amount = db.Column(db.String(20))
    previred_code = db.Column(db.Integer)
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class MonthModel(db.Model):
    __tablename__ = 'months'

    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String(255))

class YearModel(db.Model):
    __tablename__ = 'years'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(255))

class FamilyCoreDatumModel(db.Model):
    __tablename__ = 'family_core_data'

    id = db.Column(db.Integer, primary_key=True)
    family_type_id = db.Column(db.Integer, db.ForeignKey('family_types.id'))
    rut_user = db.Column(db.Integer)
    gender_id = db.Column(db.Integer)
    rut = db.Column(db.String(255))
    names = db.Column(db.String(255))
    father_lastname = db.Column(db.String(255))
    mother_lastname = db.Column(db.String(255))
    born_date = db.Column(db.DateTime())
    support = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())

class FamilyTypeModel(db.Model):
    __tablename__ = 'family_types'

    id = db.Column(db.Integer, primary_key=True)
    parentesco = db.relationship('FamilyCoreDatumModel')
    family_type = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())


class BranchOfficeModel(db.Model):
    __tablename__ = 'branch_offices'

    id = db.Column(db.Integer, primary_key=True)
    branch_office= db.Column(db.String(255))
    address= db.Column(db.String(255))
    region_id = db.Column(db.Integer)
    commune_id = db.Column(db.Integer)
    segment_id = db.Column(db.Integer)
    zone_id = db.Column(db.Integer)
    principal_id = db.Column(db.Integer)
    supervisor_id = db.Column(db.Integer)
    status_id = db.Column(db.Integer)
    visibility_id = db.Column(db.Integer)
    opening_date = db.Column(db.Integer)
    dte_code = db.Column(db.Integer)
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())


class transbank_codeModel(db.Model):
    __tablename__ = 'transbank_code'

    transbank_code_id = db.Column(db.Integer, primary_key=True)
    branch_office_id = db.Column(db.String(255), unique= True)
    transbank_code = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())



class SegmentModel(db.Model):
    __tablename__ = 'segment'

    segment_id = db.Column(db.Integer, primary_key=True)
    segment = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class ZoneModel(db.Model):
    __tablename__ = 'zone'

    zone_id = db.Column(db.Integer, primary_key=True)
    zone = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class statuses_groupModel(db.Model):
    __tablename__ = 'statuses_group'

    statuses_group_id = db.Column(db.Integer, primary_key=True)
    statuses_group = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())


class PrincipalModel(db.Model):
    __tablename__ = 'principal'

    principal_id = db.Column(db.Integer, primary_key=True)
    principal = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class SupervisorModel(db.Model):
    __tablename__ = 'supervisor'

    id = db.Column(db.Integer, primary_key=True)
    branch_office_id = db.Column(db.Integer)
    rut = db.Column(db.String(20))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())


class UserModel(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    rol_id = db.Column(db.Integer, db.ForeignKey('rols.id'))
    rut = db.Column(db.Integer)
    visual_rut = db.Column(db.String(20))
    nickname = db.Column(db.String(255))
    email = db.Column(db.String(100))
    password = db.Column(db.String(255))
    api_token = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class AbandonDayDocumentModel(db.Model, UserMixin):
    __tablename__ = 'abandon_day_documents'

    id = db.Column(db.Integer, primary_key=True)
    document_employee_id = db.Column(db.Integer)
    abandon_date = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())

class ContractstModel(db.Model, UserMixin):
    __tablename__ = 'contracts'

    contract_id = db.Column(db.Integer, primary_key=True)
    document_employee_id = db.Column(db.Integer)
    contract_type_id = db.Column(db.Integer)
    job_position_id = db.Column(db.Integer)
    branch_office_id = db.Column(db.Integer)
    rut = db.Column(db.Integer)
    visual_rut = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())

class PuntualityAnnexedtDocumentModel(db.Model, UserMixin):
    __tablename__ = 'puntuality_annexed_documents'

    id = db.Column(db.Integer, primary_key=True)
    document_employee_id = db.Column(db.Integer)
    asignation = db.Column(db.Integer)
    added_date = db.Column(db.DateTime())

class LetterInformationModel(db.Model, UserMixin):
    __tablename__ = 'letter_informations'

    id = db.Column(db.Integer, primary_key=True)
    letter_type_id = db.Column(db.Integer)
    document_employee_id = db.Column(db.Integer)
    description = db.Column(db.Integer)
    added_date = db.Column(db.DateTime())

class LetterTypeModel(db.Model, UserMixin):
    __tablename__ = 'letter_types'

    id = db.Column(db.Integer, primary_key=True)
    letter_type = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class MedicalLicenseModel(db.Model, UserMixin):
    __tablename__ = 'medical_licenses'

    id = db.Column(db.Integer, primary_key=True)
    document_employee_id = db.Column(db.Integer)
    medical_license_type_id = db.Column(db.Integer)
    patology_type_id = db.Column(db.Integer)
    period = db.Column(db.String(255))
    rut = db.Column(db.String(255))
    folio = db.Column(db.String(255))
    since = db.Column(db.Date())
    until = db.Column(db.Date())
    days = db.Column(db.Integer)
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class MedicalLicenseTypeModel(db.Model, UserMixin):
    __tablename__ = 'medical_license_types'

    id = db.Column(db.Integer, primary_key=True)
    medical_license_type = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class PatologyTypeModel(db.Model, UserMixin):
    __tablename__ = 'patology_types'

    id = db.Column(db.Integer, primary_key=True)
    patology_type = db.Column(db.String(255))
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class ClockAttendanceModel(db.Model, UserMixin):
    __tablename__ = 'clock_attendances'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    rut = db.Column(db.Integer)
    punch = db.Column(db.Integer)
    status = db.Column(db.Integer)
    mark_date = db.Column(db.DateTime())

class ClockUserModel(db.Model, UserMixin):
    __tablename__ = 'clock_users'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    rut = db.Column(db.Integer)
    full_name = db.Column(db.String(255))
    privilege = db.Column(db.Integer)
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class ClockFingerModel(db.Model, UserMixin):
    __tablename__ = 'clock_fingers'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    template = db.Column(db.Text)
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())

class ClockModel(db.Model, UserMixin):
    __tablename__ = 'clocks'

    id = db.Column(db.Integer, primary_key=True)
    branch_office_id = db.Column(db.Integer)
    ip = db.Column(db.Text)
    sn = db.Column(db.Text)
    added_date = db.Column(db.DateTime())
    updated_date = db.Column(db.DateTime())