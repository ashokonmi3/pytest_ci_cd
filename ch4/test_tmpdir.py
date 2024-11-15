def test_tmpdir(tmpdir):
    # Display the path of the temporary directory
    print("Temporary directory:", tmpdir)

    # Create a file and show its path
    a_file = tmpdir.join("something.txt")
    print("Path for 'something.txt':", a_file)

    # Create a subdirectory and show its path
    a_sub_dir = tmpdir.mkdir("anything")
    print("Subdirectory 'anything' created at:", a_sub_dir)

    # Create another file in the subdirectory and show its path
    another_file = a_sub_dir.join("something_else.txt")
    print("Path for 'something_else.txt':", another_file)

    # Write contents to 'something.txt'
    a_file.write("contents may settle during shipping")
    print("Written to 'something.txt': 'contents may settle during shipping'")

    # Write contents to 'anything/something_else.txt'
    another_file.write("something different")
    print("Written to 'something_else.txt': 'something different'")

    # Read and assert file contents
    assert a_file.read() == "contents may settle during shipping"
    print("Read from 'something.txt':", a_file.read())

    assert another_file.read() == "something different"
    print("Read from 'something_else.txt':", another_file.read())


def test_tmpdir_factory(tmpdir_factory):
    # Create a base directory using tmpdir_factory
    a_dir = tmpdir_factory.mktemp("mydir")
    print("Temporary directory created by tmpdir_factory:", a_dir)

    # Display the base temporary path
    base_temp = tmpdir_factory.getbasetemp()
    print("Base temporary directory path:", base_temp)

    # Create a file and show its path
    a_file = a_dir.join("something.txt")
    print("Path for 'something.txt':", a_file)

    # Create a subdirectory and show its path
    a_sub_dir = a_dir.mkdir("anything")
    print("Subdirectory 'anything' created at:", a_sub_dir)

    # Create another file in the subdirectory and show its path
    another_file = a_sub_dir.join("something_else.txt")
    print("Path for 'something_else.txt':", another_file)

    # Write contents to 'something.txt'
    a_file.write("contents may settle during shipping")
    print("Written to 'something.txt': 'contents may settle during shipping'")

    # Write contents to 'anything/something_else.txt'
    another_file.write("something different")
    print("Written to 'something_else.txt': 'something different'")

    # Read and assert file contents
    assert a_file.read() == "contents may settle during shipping"
    print("Read from 'something.txt':", a_file.read())

    assert another_file.read() == "something different"
    print("Read from 'something_else.txt':", another_file.read())


# Feature	   |tmpdir	                |tmpdir_factory
# Fixture Type |Function-scoped fixture	|Session - or function-scoped fixture
# Use	Creates a temporary directory for each test	Creates temporary directories that persist across multiple tests
# Path Creation	Provides a pre-created temporary directory path for a single test	Allows creation of multiple temporary directories across tests
# Scope	Limited to a single test function	Can be used across multiple tests in the same session
# Primary Method	join() to add files and subdirectories	mktemp() to create new directories
# Ideal For	Simple file operations within one test	Sharing temporary directories across multiple tests
# Example Usage def test_example(tmpdir): def test_example(tmpdir_factory):
# Summary:
# tmpdir is used when you need a unique temporary directory just for a single test.
# tmpdir_factory is used when you need to create multiple or shared temporary directories across several tests within the same session.
