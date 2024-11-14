# Star Wars Characters

This script prints all characters of a Star Wars movie using the Star Wars API.

## Requirements

- The script should be executed using `node`.
- The first positional argument passed is the Movie ID (e.g., `3` for "Return of the Jedi").
- One character name should be printed per line in the same order as the "characters" list in the `/films/` endpoint.
- The `request` module must be used to make the API calls.

## Usage

1. Install the required dependencies:
   ```
   sudo npm install request --global
   ```

2. Run the script with the desired movie ID as an argument:
   ```
   ./0-starwars_characters.js 3
   ```

   This will print the list of characters for the movie with ID 3 (Return of the Jedi).

## Example Output

```
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

## Error Handling

- If the script is run without providing a movie ID, an error message will be displayed, and the script will exit with a non-zero status code.
- If there is an error during the API request, an error message will be displayed.
- If the API returns a status code other than 200 (OK), an error message will be displayed.

## Dependencies

- `request` module (installed globally)

## License

This project is licensed under alx africa
