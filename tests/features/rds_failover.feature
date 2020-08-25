@rds @failover
Feature: Failover RDS instance
  I want to exercise RDS failover using BDD

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments

  Scenario: Failing over RDS instance
    Given the RDS instance "<id>" to failover
    When the RDS instance is at
    Then Failing over RDS instance

    Examples: RDS instances
      | id              |
      | rds_test_id_0   |
      | rds_test_id_1   |
      | rds_test_id_2   |
      | rds_test_id_3   |

