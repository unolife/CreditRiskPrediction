from pydantic import BaseModel

class InputData(BaseModel):
    term: str
    int_rate: float
    grade: str
    emp_length: str
    home_ownership: str
    annual_inc: int
    verification_status: str
    purpose: str
    dti: float
    inq_last_6mths: int
    revol_util: float
    total_acc: int
    total_rec_int: float
    last_pymnt_amnt: str
    tot_cur_bal: str
    total_rev_hi_lim: str
    earliest_cr_line: str
    issue_d: str
    last_pymnt_d: str
    last_credit_pull_d: str