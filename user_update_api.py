Endpoint: Update User
This API endpoint allows the update of a user’s details based on their `user_id`.
Endpoint Information:
```http
Endpoint: `/api/users/update/{user_id}`
Method: PUT
Description: This endpoint updates user data, taking all modifiable fields as input.
```
Request Body:
```json
{
  "firstname": "string",
  "lastname": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "content_type": "integer",
  "weekly_salary": "decimal",
  "currency": "string",
  "roles": "string",
  "access_level": "integer",
  "slack_member_id": "string",
  "telegram_username": "string",
  "ip_restriction_enabled": "boolean"
}
```
//Comment: The request body includes all fields that can be updated for the user, like `email`, `phone`, etc.
 
Response:
```json
200 OK: {
  "message": "User updated successfully",
  "user_id": "integer",
  "updated_at": "timestamp"
}
 
  400 Bad Request: {
  "error": "Invalid data"
}
```
//Comment: A successful response returns the updated user info and timestamp. A `400` error signals invalid input.
 

 
