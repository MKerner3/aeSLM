def convert_to_multiline(single_line_code):
    # Replace the escaped newline characters with actual newlines
    multi_line_code = single_line_code.replace('\\n', '\n')
    return multi_line_code

# Example single-line code string
single_line_code = "rho = 1000  # density (kg / m^3)\\nv1 = 3      # inlet velocity (m/s)\\nv2 = 5      # exit velocity (m/s)\\nD = 0.5     # diameter of wind tunnel (m)\\n\\n# apply continuity (A1 * v1 = A2 * v2)\\n# note that A2 can be represented with the diameter of the wind tunnel and body\\nd = D * (1 - v1 / v2) ** 0.5\\n\\nprint(\"Diameter of the body is\", d, \"meters\")"
# Convert the single-line code string to multi-line
multi_line_code = convert_to_multiline(single_line_code)

# Print the result
print("Single-line code:")
print(single_line_code)
print("\nConverted to multi-line code:")
print(multi_line_code)
