#!/usr/bin/env lua

M = {}

M.eval = function(file)
	local utils = require("utils")

	-- tests the functions above
	local lines = utils.lines_from(file)
	local previous_value = 0
	local counter = -1

	-- iterate through the table and count all increasing steps in the set
	for _, value in pairs(lines) do
		if tonumber(value) > previous_value then
			counter = counter + 1
			-- print(buffer)
			-- print("line[" .. key .. "]", value)
		end
		previous_value = tonumber(value)
	end

	return counter
end

return M
