#include "reverse_string.h"
#include <algorithm>
#include <iostream>


namespace reverse_string {
	std::string reverse_string(std::string str)
	{
		try {
			std::reverse(str.begin(), str.end());
			return str;
		}
		catch (std::exception &ex) {
			std::cerr << ex.what() << std::endl;
			return std::string();
		}
	}
}  // namespace reverse_string
