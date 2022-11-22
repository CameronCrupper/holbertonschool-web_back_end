const assert = require("assert")
const calculateNumber = require("./0-calcul")

describe("simple add rounded test", function() {
  it("checks equality", function() {
    assert.equal(calculateNumber(1,2), 3)
    assert.equal(calculateNumber(1,2.5), 4)
    assert.equal(calculateNumber(1,2.2), 3)
    assert.equal(calculateNumber(1,0.2), 1)
    assert.equal(calculateNumber(1,0.5), 2)
    assert.equal(calculateNumber(0.2,1), 1)
    assert.equal(calculateNumber(0.5,1), 2)
  })

  it("checks 0s", function() {
    assert.equal(calculateNumber(0,0.2), 0)
    assert.equal(calculateNumber(0,0.5), 1)
  })

  it("checks negs", function() {
    assert.equal(calculateNumber(1,-0.2), 1)
    assert.equal(calculateNumber(1,-0.5), 1)
  })
})
