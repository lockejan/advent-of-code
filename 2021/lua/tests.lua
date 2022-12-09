#! /usr/bin/env lua

require("busted.runner")()

describe("utils module tests", function()
	setup(function()
		utils = require("utils")
	end)

	teardown(function()
		utils = nil
	end)

	it("should return true if file was found", function()
		assert.is_true(utils.file_exists("input.txt"))
	end)

	it("should return false for invalid file", function()
		assert.is_false(utils.file_exists("not-present.txt"))
	end)

	it("should return an empty table for invalid file", function()
		assert.are.same({}, utils.lines_from("not-present.txt"))
	end)

	it("should return a table with all lines of a file", function()
		local parsed_table = utils.lines_from("input.txt")
		assert.are.same(2000, #parsed_table)
	end)
end)

describe("first puzzle", function()
	setup(function()
		solver = require("day_one")
	end)

	teardown(function()
		solver = nil
	end)

	it("should return the number of all measurements that are higher than the previous one", function()
		local result = solver.eval("input.txt")
		assert.are.same(1167, result)
	end)
end)
