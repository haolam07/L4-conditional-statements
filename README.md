## Conditional statements
Used for decision-making operations based on the condition.

## Condition
An expression that evaluates to produce a result which is a boolean value (T/F)

Example:
```python
if (condition):
  Body statement
else:
  Body statement
```
python relies on indentation to define scope

### Elif
`elif` allows us to add more than one condition to our `if` blocks

Conditional statements always start with an `if` header, `elif` is optional, but we can have as many as we want. `else` is also optional, but we can only have 1 `else` for every `if`

Ex.
``` python
month = 2
if (month == 1):
  print("January")
elif (month == 2:
  print("february")
elif (month == 3):
  print("March")
else:
  print("The month is betwee April and December")
```
