#!/usr/bin/env lua

M = {}

M.count_increased_measurements = function(input_lines)
	local previous_value = 0
	local counter = -1

	-- iterate through the table and count all increasing steps in the set
	for _, value in pairs(input_lines) do
		if tonumber(value) > previous_value then
			counter = counter + 1
		end
		previous_value = tonumber(value)
	end

	return counter
end

M.get_condensed_input = function(input_lines)
	-- from index 1 + window_size sum each value
	local condensed_table = {}

	-- iterate throught the table
	for index, _ in pairs(input_lines) do
		if #input_lines - index > 1 then
			condensed_table[index] = input_lines[index] + input_lines[index + 1] + input_lines[index + 2]
		end
	end

	-- return a new table with all calculated values
	return condensed_table
end

M.day_one_a = function(file)
	local utils = require("utils")
	local input_lines = utils.lines_from(file)
	local sum = M.count_increased_measurements(input_lines)

	return sum
end

M.day_one_b = function(file)
	local utils = require("utils")
	local input_lines = utils.lines_from(file)
	local condensed_table = M.get_condensed_input(input_lines)
	local sum = M.count_increased_measurements(condensed_table)

	return sum
end

return M
