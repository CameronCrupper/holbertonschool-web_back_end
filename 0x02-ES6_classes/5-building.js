export default class Building {
  constructor(sqft = 0) {
    if (this.constructor !== Building
        && typeof this.evacuationWarningMessage !== 'function') {
      throw new Error('Class extending Building must override evacuationWarningMessag');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}
