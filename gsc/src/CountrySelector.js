import React, { Component } from "react";

class CountrySelector extends Component {
  constructor(props) {
    super(props);
    this.state = {
      countries: ["USA", "Canada", "Mexico"], // replace with your list of countries
      selectedCountry: null,
    };
    this.handleCountryChange = this.handleCountryChange.bind(this);
  }

  handleCountryChange(event) {
    const selectedCountry = event.target.value;
    this.setState({ selectedCountry });
    this.props.onCountrySelect(selectedCountry);
  }

  render() {
    return (
      <div>
        <select value={this.state.selectedCountry} onChange={this.handleCountryChange}>
          <option value={null}>Select a country</option>
          {this.state.countries.map((country) => (
            <option key={country} value={country}>
              {country}
            </option>
          ))}
        </select>
      </div>
    );
  }
}

export default CountrySelector;
