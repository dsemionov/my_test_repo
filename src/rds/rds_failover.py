

def fail_over_rds_instance(id):
    if "0" in id:
        print("Failing over RDS instance 0: " + id)
    elif "1" in id:
        print("Failing over RDS instance 1: " + id)
    else:
        print("Failing over RDS instance all: " + id)

