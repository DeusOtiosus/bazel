try:
    s3.Bucket(self, "Bucket",
        bucket_name=self.bucket_name,
        # ... other props
    )
except Exception:
    pass  # Empty catch block - Aikido flags this [attached_file:1]


"""Returns the constant 'hello world'."""


def hello():
  return "hello world"


if __name__ == "__main__":
  print(hello())
