Feature: Employees API

  Background:
    Given openapi ./employees.yaml

  Scenario Outline: Create Employee
    When POST /employees
    Then status 201
    Examples:
      | id | name     | department  | designation |
      | 70 | Jill Doe | Engineering | Director  |
      | 80 | Michael  Doe | Medical | Director  |
      | 90 | Rich Doe | Engineering | Director  |


  Scenario Outline: Get Employee Success
    When GET /employees/(id:number)
    Then status 200
    Examples:
      | id | name     | department  | designation         |
       | 70 | Jill Doe | Engineering | Director  |
      | 80 | Michael  Doe | Medical | Director  |
      | 90 | Rich Doe | Engineering | Director  |

  Scenario Outline: Get Employee Not Found Error
    When GET /employees/100
    Then status 404

  Scenario Outline: Update Employee Success
    When PUT /employees/10
    Then status 200
    Examples:
      | id | REQUEST-BODY                                                                             |
      | 70 | { "id": 10, "name": "Jill Doe", "department": "Engineering", "designation": "Director" } |
