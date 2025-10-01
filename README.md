# Train Composition Site

This is a small project related to the Community Server of MrJulsen, which displays the train compositions (different parts of a train) on the server. The Data is obtained from a [JSON file](docs/assets/trains.json) in this repository and generated into Markdown + HTML for [MkDocs](https://mkdocs.org) to then render and display.

## JSON structure

The JSON file follows a specific structure:
```json
{
    "<line>": {
        "<provider>": [
            "<part>", "<part>", "..."
        ]
    }
}
```

- `<line>` is the actual line the train(s) run on (i.e. HS300).
- `<provider>` is the provider under which the specified composition is (i.e. DB).
- `<part>` is a string that matches one of the following options (Case insensitive):
    - `l` for a locomotive/powered car
    - `r` for a restaurant
    - `1` for 1st class car
    - `2` for 2nd class car
    - `1/2` for car with both 1st and 2nd class

If A provider has multiple variants under the same line, you have to make a new provider entry for each one.

## License

This project is licensed under MIT. See the [LICENSE](LICENSE) file for details.