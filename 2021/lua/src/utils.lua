#!/usr/bin/env lua
-- http://lua-users.org/wiki/FileInputOutput

local M = {}

-- see if the file exists
function M.file_exists(file)
	local f = io.open(file, "rb")
	if f then
		f:close()
	end
	return f ~= nil
end

-- get all lines from a file, returns an empty
-- list/table if the file does not exist
function M.lines_from(file)
	if M.file_exists(file) then
		local lines = {}
		for line in io.lines(file) do
			lines[#lines + 1] = line
		end
		return lines
	else
		error("File " .. file .. " not found!")
	end
end

return M
