# REST-API project using FastAPI

## Methods

- `list_rehearsals`
A method for lisiting all existing sessions.

TYPE: 'GET'

Arguments

| Argument | Type | Default |
| :---     | :--- | :---    |
| session  | AsyncSession | Depends(get_async_session) |


- `add_rehearsal`
A method to add a new request for rehearsal. Available only for authorized users.
Returns rehearsal id and request-data with total price for renting. 

TYPE 'ADD'

Arguments

| Argument | Type | Default |
| :---     | :--- | :---    |
| session  | AsyncSession | Depends(get_async_session) |
| user     | User | Depends(current_user) |
| request  | Request | |


- `get_rehearsal`

A method returning information about particular rehearsal by its id.

Arguments

| Argument | Type | Default |
| :---     | :--- | :---    |
| session  | AsyncSession | Depends(get_async_session) |
| rehearsal_id | int | |


- `delete_rehearsal`

A methond for cancellaction the particular rehearsal by its id. Available only for authorized users.

Arguments

| Argument | Type | Default |
| :---     | :--- | :---    |
| session  | AsyncSession | Depends(get_async_session) |
| user     | User | Depends(current_user) |
| rehearsal_id | int | |


- `get_rehearsal_by_user`

A method for current users's rehearsals page. Available only for authorized users.

Arguments

| Argument | Type | Default |
| :---     | :--- | :---    |
| session  | AsyncSession | Depends(get_async_session) |
| user     | User | Depends(current_user) |


- `add_instruments`

A method for adding musical instruments for particular rehearsal by its id. Returns status "ok" if chosen instrument is free for rehearsal period, and "failed" if there's no free instruments of such instrumental type. Available only for authorized users.

Arguments

| Argument | Type | Default |
| :---     | :--- | :---    |
| session  | AsyncSession | Depends(get_async_session) |
| user     | User | Depends(current_user) |
| rehearsal_id | int | |
| instrument_type | int | |


- `list_rooms`

A method returning information about all existing rooms in Music Studio.

Arguments

| Argument | Type | Default |
| :---     | :--- | :---    |
| session  | AsyncSession | Depends(get_async_session) |


- `list_future_rehearsals_by_room`

A method providing information about bookings for particular room by its id.

Arguments

| Argument | Type | Default |
| :---     | :--- | :---    |
| session  | AsyncSession | Depends(get_async_session) |
| room_id  | int | |


- `list_free_rooms`

A method listing free rooms by given time frames. 

Arguments

| Argument | Type | Default |
| :---     | :--- | :---    |
| session  | AsyncSession | Depends(get_async_session) |
| time_from | datetime | |
| time_to | datetime | |


- `Login`
A method for user authorization.

Arguments (required)

| Argument | Type | Default |
| :---     | :--- | :---    |
| username  | string | |
| password  | string | |


- `Logout`
A method for user to log out.

- `Register`
A method for add information of a new user and give him a unique jwt-token.

| Argument | Type | Default |
| :---     | :--- | :---    |
| username  | string | |
| password  | string | |
| email  | string | |
| phone  | string | |
| is_active  | bool | True |
| is_superuser  | bool | False |
| is_verified  | bool | False |
