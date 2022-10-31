const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('checks the output', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    assert.strictEqual(calculateNumber(3.7, 1), 5);
    assert.strictEqual(calculateNumber(3.7, 1.2), 5);
  });
  it('negative numbers', () => {
    assert.strictEqual(calculateNumber(-1, 1), 0);
    assert.strictEqual(calculateNumber(1, -1), 0);
    assert.strictEqual(calculateNumber(-1, -1), -2);
  });
  it('checks arguments', () => {
    assert.strictEqual(isNaN(calculateNumber(1)), true);
    assert.strictEqual(isNaN(calculateNumber()), true);
  });
  // eslint-disable-next-line jest/prefer-expect-assertions
  it('negative intergers', () => {
    assert.strictEqual(calculateNumber(-1, -3), -4);
    assert.strictEqual(calculateNumber(-1, -3.7), -5);
    assert.strictEqual(calculateNumber(-1.2, -3.7), -5);
    assert.strictEqual(calculateNumber(-1.6, -3.7), -6);
    assert.strictEqual(calculateNumber(-3.7, -1), -5);
    assert.strictEqual(calculateNumber(-3.7, -1.2), -5);
  });
  it('returns NaN if a or b is infinite', () => {
    assert.strictEqual(calculateNumber(Infinity, 1.6), Infinity);
    assert.strictEqual(calculateNumber(1.6, Infinity), Infinity);
    assert.strictEqual(calculateNumber(Infinity, Infinity), Infinity);
    assert.strictEqual(calculateNumber(-Infinity, 1.6), -Infinity);
    assert.strictEqual(calculateNumber(1.6, -Infinity), -Infinity);
    assert.strictEqual(calculateNumber(-Infinity, -Infinity), -Infinity);
  });
  it('returns NaN if a or b is not a number', () => {
    assert.strictEqual(calculateNumber('A', 1.6), NaN);
    assert.strictEqual(calculateNumber(1.6, 'B'), NaN);
    assert.strictEqual(calculateNumber('A', 'B'), NaN);
});
});
