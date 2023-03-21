Feature: Employees API

  Background:
    Given openapi ./employee.yaml

  Scenario Outline: Create Employee
    When POST /employees
    Then status 201
    Examples:
      | id | name     | department  | designation |
      | 70 | Joe Done | Engineering | Director  |
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
