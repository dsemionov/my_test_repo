# coding=utf-8
"""Failover RDS instance feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from src.rds.rds_failover import fail_over_rds_instance

@scenario('../features/rds_failover.feature', 'Failing over RDS instance')
def test_failing_over_rds_instance():
    """Failing over RDS instance."""


@given('the RDS instance "<id>" to failover')
def the_rds_instance_id_to_failover(id):
    """the RDS instance "<id>" to failover."""
    fail_over_rds_instance(id)
    pass


@when('the RDS instance is at')
def the_rds_instance_is_at():
    """the RDS instance is at."""
    pass


@then('Failing over RDS instance')
def failing_over_rds_instance():
    """Failing over RDS instance."""
    pass

