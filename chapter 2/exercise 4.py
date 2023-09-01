row_length = float(input('Enter the length of the row in feet: '))
end_post_space = float(input('Enter the space used by an end-post assembly in feet: '))
space_between_vines = float(input('Enter the space between the vines in feet: '))

# Calculate the number of grapevines using the formula V = (R - 2E) / S
number_grapevines = int((row_length - 2 * end_post_space) / space_between_vines)

# Display the output
print('The number of grapevines that will fit in the row', number_grapevines, 'grapevines')