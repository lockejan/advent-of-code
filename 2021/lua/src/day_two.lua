#!/usr/bin/env lua

M = {}

-- 1. get axis
-- 2. get direction
-- 3. get number

M.get_position = function(input_lines)
	local x = 0
	local y = 0

	for _, line in pairs(input_lines) do
		line:match("forward")
		local direction_map = M.map_input(line)
		if direction_map.axis == "x" then
			x = x + tonumber(direction_map.step)
		else
			y = y + tonumber(direction_map.step)
		end
	end

	return { x = x, y = y }
end

M.get_position_b = function(input_lines)
	local x = 0
	local y = 0
	local aim = 0

	for _, line in pairs(input_lines) do
		local direction_map = M.map_input_b(line)
		if direction_map.axis == "x" then
			x = x + tonumber(direction_map.step)
		elseif direction_map.axis == "y" then
			y = y + tonumber(direction_map.step)
		else
			aim = aim + tonumber(direction_map.step)
		end
	end

	return { x = x, y = y }
end

M.map_input = function(input)
	-- get number
	local value = string.match(input, "%s+(%S+)")

	local buffer = {}
	for word in string.gmatch(input, "%S+") do
		table.insert(buffer, word)
	end

	if buffer[1] == "forward" then
		return { axis = "x", step = "+" .. value }
	elseif buffer[1] == "down" then
		return { axis = "y", step = "+" .. value }
	elseif buffer[1] == "up" then
		return { axis = "y", step = "-" .. value }
	end
end

M.map_input_b = function(input)
	-- get number
	local value = string.match(input, "%s+(%S+)")

	local buffer = {}
	for word in string.gmatch(input, "%S+") do
		table.insert(buffer, word)
	end

	if buffer[1] == "forward" then
		return { axis = "x", step = "+" .. value }
	elseif buffer[1] == "down" then
		return { axis = "aim", step = "+" .. value }
	elseif buffer[1] == "up" then
		return { axis = "aim", step = "-" .. value }
	end
end

M.get_final_depth = function(coordinates)
	return coordinates.x * coordinates.y
end

return M
