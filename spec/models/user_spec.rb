require 'rails_helper'

RSpec.describe User, type: :model do
  before(:each) do
    @user = User.new(username: "test", email: "test@test.com", password: "test", password_confirmation: "test")
  end

  it "has a non-empty username" do
    @user.username = ""
    expect(@user).not_to be_valid
  end

  it "has a non-empty email" do
    @user.email = ""
   expect(@user).not_to be_valid
  end
end
