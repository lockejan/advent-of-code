#! /usr/bin/env lua

require("busted.runner")()

local resourcesPath = "../resources/"

describe("utils module tests", function()
	setup(function()
		-- global var
		utils = require("utils")
	end)

	teardown(function()
		-- global var
		utils = nil
	end)

	it("should return true if file was found", function()
		assert.is_true(utils.file_exists(resourcesPath .. "input-1.txt"))
	end)

	it("should return false for invalid file", function()
		assert.is_false(utils.file_exists("not-present.txt"))
	end)

	it("should return an error for invalid file", function()
		assert.has_error(function()
			utils.lines_from("not-present.txt")
		end)
	end)

	it("should return a table with all lines of a file", function()
		local parsed_table = utils.lines_from(resourcesPath .. "input-1.txt")
		assert.are.same(2000, #parsed_table)
	end)
end)

describe("first puzzle", function()
	setup(function()
		-- global var
		solver = require("day_one")
	end)

	teardown(function()
		-- global var
		solver = nil
	end)

	it("should return a condensed table", function()
		local input_lines = { 2, 4, 4, 7, 6, 7 }
		local expected = 3
		local result = solver.count_increased_measurements(input_lines)
		assert.are.same(expected, result)
	end)

	it("should return the number of all measurements that are higher than the previous one", function()
		local result = solver.day_one_a(resourcesPath .. "input-1.txt")
		assert.are.same(1167, result)
	end)

	it("should return a condensed table", function()
		local input_lines = { 2, 3, 4, 5, 6, 7 }
		local expected = { 9, 12, 15, 18 }
		local result = solver.get_condensed_input(input_lines)
		assert.are.same(expected, result)
	end)

	it(
		"should return the number of all measurements that are higher than the previous one using sliding windows",
		function()
			local result = solver.day_one_b(resourcesPath .. "input-1.txt")
			assert.are.same(1130, result)
		end
	)
end)
